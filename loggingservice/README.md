# Logging Building Block

The goal of the Logging Building Block is to provide a set of RESTFul web services to log all the activities of the bp.
                      

## Setup Environment
```
cd loggingservice
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run in Development Mode

```
cd rokwire-building-blocks-api
export FLASK_APP=loggingservice
export FLASK_ENV=development
flask run
```
and the Logging Building Block should be running at localhost at port 5000 (http://localhost:5000/logs).
The detailed API information is in rokwire.yaml in the OpenAPI Spec 3.0 format.

## Run as Docker Container in Local
```
cd loggingservice
./docker.sh
docker run --rm --name logging -e LOGGING_MONGO_URL=mongodb://mongodb_ip_address:mongodb_port -e LOGGING_URL_PREFIX=<url_prefix_starting_with_slash> -p 5000:5000 rokwire/logging-building-block
```
You can edit config.py to specify mongo database name, collection name, and a URL prefix.
```
LOGGING_DB_NAME="loggingdb"
LOGGING_COLL_NAME="logs"
LOGGING_URL_PREFIX="/logs"
```


## Sample Logs for Post Endpoint:

Let us use ```curl``` command to post two sample events to the Events Building Block running at `http://localhost:5000/logs`.

```
curl -d '{
            "timestamp": "2019-06-01T10:15:23Z",
            "uuid": "56fe224b-3600-4b66-ac8d-5d2906e19fc61",
            "os": "ios",
            "osVersion": "10.1.4",
            "appVersion": "1.2",
            "device": "iphone 7",
            "deviceSettings": {
                "description": "test device description",
                "setting": "test setting"
            },
            "userAction": {
                "description": "test description",
                "type": "test type",
                "name": "test name",
                "mainFeature": "test main feature",
                "subFeature": "test sub feature",
                "customAttribute1": "test custom attribute 1",
                "customAttribute2": "test custom attribute 2",
                "customAttribute3": "test custom attribute 3",
                "customAttribute4": "test custom attribute 4",
                "customAttribute5": "test custom attribute 5"
            }
}' -H "Content-Type: application/json" -X POST http://localhost:5000/logs
```

It will return back the `post` status in json which includes the internal id as below:

```
{
    message": "[POST]: logging record posted: uuid = 56fe224b-3600-4b66-ac8d-5d2906e19fc61",
    "status": 201,
    "uuid": "56fe224b-3600-4b66-ac8d-5d2906e19fc61"
}
```

