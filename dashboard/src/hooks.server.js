import PocketBase from 'pocketbase';
import { env } from '$env/dynamic/public';

export const handle = async ({ event, resolve }) => {
  event.locals.pb = new PocketBase(env.PUBLIC_POCKETBASE_URL || 'https://localhost:8090');
  event.locals.pb.authStore.loadFromCookie(event.request.headers.get('cookie') || '');

  event.locals.pb.autoCancellation(false);

  if (event.locals.pb.authStore.isValid) {
    event.locals.user = structuredClone(event.locals.pb.authStore.model);
  } else {
    event.locals.user = undefined;
  }

  const response = await resolve(event);
  response.headers.set('set-cookie', event.locals.pb.authStore.exportToCookie());
  return response;
};
