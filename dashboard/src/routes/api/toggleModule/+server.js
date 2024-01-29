import { error } from '@sveltejs/kit';

export async function POST({ request, locals }) {
  const { moduleName } = await request.json();

  try {
    const fullList = await locals.pb.collection('enabled_modules').getFullList();

    if (fullList.length > 0) {
      const foundModule = fullList.find((el) => el.name === moduleName);

      if (foundModule.id) {
        await locals.pb.collection('enabled_modules').delete(foundModule.id);
      } else {
        await locals.pb.collection('enabled_modules').create({ name: moduleName });
      }
    } else {
      await locals.pb.collection('enabled_modules').create({ name: moduleName });
    }

    return new Response({
      success: true
    });
  } catch (err) {
    console.log(err);
    throw error(500, 'Something went wrong.');
  }
}
