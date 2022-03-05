# Abstract Factory

Training Abstract Factory method with Python.

## Annotations

- Concrete Products populates the setter method (Concrete Factory);
- Setter method (Concrete Factory) choise what type of product must be returned based on input product field;
- Setter method (Concrete Factory) returns a concrete product;
- Decorate method calls create_product method (Abstract Factory);
- create_product method (Abstract Factory) calls setter method;
- create_product method (Abstract Factory) calls make method (Concrete Product)
- create_product method (Abstract Factory) returns a concrete product;

## Requirements

- Python >= 3.7

## Usage

```sh
python3 -u factory-method
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)