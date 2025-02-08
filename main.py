from fastapi import FastAPI, Query
import math

app = FastAPI()

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def get_fun_fact(n: int) -> str:
    """Generate a fun fact about the number."""
    facts = []
    if is_prime(n):
        facts.append(f"{n} is a prime number.")
    if is_perfect(n):
        facts.append(f"{n} is a perfect number.")
    if is_armstrong(n):
        facts.append(f"{n} is an Armstrong number.")
    return " ".join(facts) if facts else f"{n} is just a normal number."

@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="The number to classify")):
    """Classify a number and return its properties."""
    properties = []
    if is_prime(number):
        properties.append("prime")
    if is_perfect(number):
        properties.append("perfect")
    if is_armstrong(number):
        properties.append("armstrong")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties or ["none"],
        "digit_sum": sum(int(d) for d in str(number)),
        "fun_fact": get_fun_fact(number)
    }
