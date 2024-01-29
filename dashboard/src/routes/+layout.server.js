export const load = async ({ locals }) => {
  return {
    modules: await locals.pb.collection('enabled_modules').getFullList(),
    user: {
      name: 'Ruben Uijtdewilligen'
    }
  };
};
