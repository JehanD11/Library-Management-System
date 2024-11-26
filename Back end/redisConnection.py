import redis

def connect_to_redis():
    try:
        r = redis.Redis(
            host='localhost',  
            port=6379,         
            db=0               
        )
        if r.ping():
            print("Connected to Redis!")
        return r
    except Exception as e:
        print(f"Failed to connect to Redis: {e}")
        return None

if __name__ == "__main__":
    redis_client = connect_to_redis()

    if redis_client:
        redis_client.set('name', 'Jehan')

        name = redis_client.get('name')
        print(f"Value of 'name': {name.decode()}") 

        redis_client.set('counter', 1)
        redis_client.incr('counter')
        counter = redis_client.get('counter')
        print(f"Value of 'counter': {counter.decode()}")

        redis_client.delete('name')
        print("Deleted 'name'")
