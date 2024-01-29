export const actions = {
  deleteAllRecords: async ({ request, locals }) => {
    try {
      const records = await locals.pb.collection('sorting_machine_records').getFullList();
      records.forEach(async (record) => {
        await locals.pb.collection('sorting_machine_records').delete(record.id);
      });
    } catch (err) {
      throw error(err.status, err.message);
    }

    return {
      success: true
    };
  }
};
