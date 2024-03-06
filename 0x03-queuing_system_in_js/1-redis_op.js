import { createClient } from 'redis';

const client = createClient()
    .on('err', err => console.log('Redis client not connected to the server:', err))
    .on('connect', () => console.log('Redis client connected to the server'));

const setNewSchool = (schoolName, value) => client.set(schoolName, value, (err, reply) => {
    console.log(reply);
});

const displaySchoolValue = (schoolName) => client.get(schoolName, (err, reply) => {
    console.log(reply);
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');