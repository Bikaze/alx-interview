# 0x00. Pascal's Triangle
`Algorithm` `python`

This project is an implementation of Pascal's Triangle algorithm in Python.

## Algorithm

Pascal's Triangle is a triangular array of binomial coefficients. Each number in the triangle is the sum of the two numbers directly above it. The first and last numbers in each row are always 1.

## Usage

To use the Pascal's Triangle function, follow these steps:

1. Import the function from the `0-pascal_triangle.py` file into your Python script.
2. Call the function with the desired number of rows as an argument.
3. The function will return a list of lists representing Pascal's Triangle.

Here's an example of how to use the function:

```python
from 0-pascal_triangle import pascal_triangle

rows = 5
triangle = pascal_triangle(rows)
print(triangle)
```

This will output the following Pascal's Triangle:

```
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

