# Number Classification API

This is a Flask-based API that classifies numbers based on mathematical properties. It returns various interesting facts about a given number.

## API Endpoint

**URL**: `/api/classify-number?number={number}`

**Example**:

**Response**:
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
