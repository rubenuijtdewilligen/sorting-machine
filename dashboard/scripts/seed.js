import 'dotenv/config';
import PocketBase from 'pocketbase';

const pb = new PocketBase(process.env.PUBLIC_POCKETBASE_URL || 'https://localhost:8090');
pb.autoCancellation(false);

for (let i = 0; i < 999; i++) {
  const random = Math.random();
  const randomClass = random < 0.5 ? 1 : 2;

  pb.collection('sorting_machine_records').create({ class: randomClass });
}
