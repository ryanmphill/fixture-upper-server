# Fixture Upper API

This API currently has one job, and one job only: convert standard JSON data into Django fixtures that can be used to seed a database. 

The API is mostly designed to be used with the [Fixture Upper Client](https://github.com/ryanmphill/fixture-upper) as a part of the [Fixture Upper App](https://fixture-upper.netlify.app/), but feel free to use it with Postman as well!

![Postman Demo](./public/fixture-upper-postman-demo.gif)

### API Url
`https://fixture-upper-api-v67kh.ondigitalocean.app`

### Resources

**Method**: `POST`

**Endpoint**: `/converter`

**Body:**

```JSON
{
    "model": "Django_model_name",
    "JSON": [
        {
            "id (required)": 1,
            "example1": "example1",
            "example2": "example2"
        },
        {
            "id (required)": 2,
            "example1": "example1",
            "example2": "example2"
        }
    ]
}
```

**Response**

`200 OK`

```JSON
[
    {
        "model": "Django_model_name",
        "pk": 1,
        "fields": {
            "example1": "example1",
            "example2": "example2"
        }
    },
    {
        "model": "Django_model_name",
        "pk": 2,
        "fields": {
            "example1": "example1",
            "example2": "example2"
        }
    }
]
```
