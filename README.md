# NLPTHAI

this is api app to find keyword from text word. develop by python flask. reference NLP algorithm by [pythainlp](https://github.com/PyThaiNLP/pythainlp)

## Quick Start

To start the app:

1. Install [docker-compose](https://docs.docker.com/compose/install/) on the docker host.
1. Clone this repo on the docker host.
```bash
docker compose up 
```

To Stop the app
```bash
docker compose down 
```

## Usage
Call path url with Post /v1/nlp/cleansing 

```python
body: {
    "text": string
}
```

## License

[MIT](https://choosealicense.com/licenses/mit/)