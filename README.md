# image-clf

A project that outputs a probability of an image being one of certain classes.

The image input must be an URL. 

# Building the docker container 

In the command line type

```
docker build -t image-clf .
```

# .env parameters 

The example parameters can be found in .env_example file.

**API_KEY_1**, **API_KEY_2** - api keys from azure cloud. 

Getting the keys: https://azure.microsoft.com/en-us/try/cognitive-services/my-apis/