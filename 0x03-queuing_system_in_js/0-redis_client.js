import { createClient } from 'redis';

const client = createClient()
    .on('err', err => console.log('Redis client not connected to the server:', err))
    .on('connect', () => console.log('Redis client connected to the server'));

