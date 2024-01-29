export const load = async ({ locals }) => {
  return {
    modules: await locals.pb.collection('enabled_modules').getFullList()
  };
};

export const actions = {
  swapDate: async ({ request, locals }) => {
    const { id, date } = Object.fromEntries(await request.formData());

    try {
      await locals.pb.collection('lessonappointments').update(id, { date });
    } catch (err) {
      throw error(err.status, err.message);
    }

    return {
      success: true
    };
  }
};
