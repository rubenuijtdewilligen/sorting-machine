export const load = async ({ locals }) => {
  return {
    records: await locals.pb.collection('sorting_machine_records').getFullList({ sort: '-created' })
  };
};
