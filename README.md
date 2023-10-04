# Fetch Rewards Challenge
# Fetch Rewards Challenge

Execution of scripts, to run the script only need run it your cmd or terminal **python file_name.py** in this case first we run:
- [init_message.py](https://github.com/AlbertPlata/Fetch_Rewards_test/blob/main/init_message.py)
	With this I emulated the data received of the SQS request (I did this cos I can't access to  data sample, you find the details of this [here](https://github.com/AlbertPlata/Fetch_Rewards_test/blob/main/issues.md)

Next execution would be:
- [masking.py](https://github.com/AlbertPlata/Fetch_Rewards_test/blob/main/masking.py)
Here I used hash encryption then the encryptation created a new [JSON ](https://github.com/AlbertPlata/Fetch_Rewards_test/blob/main/masked_messages.json) file to prepare the data to be loaded.

Finally the last execution is:
- [load_data.py](https://github.com/AlbertPlata/Fetch_Rewards_test/blob/main/load_data.py)
	Here read the hashed data, connect with the database, and load using one simple thread

# Final Questions
#### How would you deploy this application in production?
To deploy this, assumption that the amount of messages is moderate, we create an AWS Lambda and run the script, obviously with the correct credentials of all the services (AWS Lambda, AWS SQS, Postgres access)
#### What other components would you want to add to make this production ready?
The answer depends on the maturity of the data pipelines
If we have small set of these  (1-3), it's a good approach use this stack, I only add cronjob on serverless architecture to deploy
 -  AWS Lambda
In another case, if we have a complex set of pipelines, consuming a lot of data sources, more than AWS SQS, i think it's appropriate use a data workflow tool.
- Apache Airflow
Cos, simplify the management of pipelines, easy scaling, and offer flexibility
#### How can this application scale with a growing dataset?
We would be on mine, that depends on two principal factors.
- The velocity of data growth, forces us to pay for update the instance capability
- The users with access to this information (analyst, data engineers, VP, etc)
	if there are hundreds of access to these resources, we need to deploy polls of 
	connection to limit the threads and control the load on the databases.
	Also, it's highly recommended to use Datawarehouse or Data Lakes, to train the 
	models and prevent  analyst and data scientist training using productive instances.
#### How can PII be recovered later on?
To find duplicated device_id

    SELECT masked_deviceid, COUNT(1) as duplicate_count
    FROM user_logins
    GROUP BY masked_device_id
    HAVING COUNT(1) > 1;
    
To find duplicated ip

	SELECT masked_ip, COUNT(1) as duplicate_count
    FROM user_logins
    GROUP BY masked_ip
    HAVING COUNT(1) > 1;
#### What are the assumptions you made?
I assume that
- There are only a few pipelines, wich is easy for the managment
- Only a few access to the database so skpi a poll connection and thread to process the messages
In both cases, they have already been explained in my judgment of scalability 
