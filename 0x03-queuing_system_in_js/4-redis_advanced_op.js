import { createClient } from 'redis';
import 'redis';

const client = createClient()
    .on('err', err => console.log('Redis client not connected to the server:', err))
    .on('connect', () => console.log('Redis client connected to the server'));

client.hSet('HolbertonSchools', 'Portland', '50', 'Seattle', '80', 'New York', '20', 'Bogota', '20', 'Cali', '40', 'Paris', '2', redis.print());
client.hGetAll('HolbertonSchools', (err, reply) => {
    console.log(reply);
});