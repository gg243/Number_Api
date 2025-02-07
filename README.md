# Number Classification API

A simple API that accepts a number and returns interesting mathematical properties about it, along with a fun fact.

## Endpoint

- **GET** `/api/funnumber?number={number}`

### Example Response (200 OK)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
