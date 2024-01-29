<script>
  import { Icon } from '@steeze-ui/svelte-icon';
  import { Trash } from '@steeze-ui/heroicons';
  import { enhance, applyAction } from '$app/forms';
  import { invalidateAll, goto } from '$app/navigation';
  import { Modal } from '$lib/components';

  let deleteModalOpen;
  let loading;

  $: deleteModalOpen = false;
  $: loading = false;

  const submitDelete = () => {
    loading = true;
    deleteModalOpen = true;
    return async ({ result }) => {
      switch (result.type) {
        case 'success':
          await invalidateAll();
          goto('/sorting-machine/settings');
          break;
        case 'error':
          break;
        default:
          await applyAction(result);
      }
      loading = false;
    };
  };
</script>

<h1 class="title text-2xl font-bold">Sorting Machine Settings</h1>

<Modal label="delete-lesson" checked={deleteModalOpen}>
  <span slot="trigger" class="btn btn-primary mt-4 text-white">
    <Icon src={Trash} size="1rem" />Delete all sorting machine data</span
  >
  <h3 slot="heading">Delete all sorting machine data</h3>
  <hr />

  <p class="mt-2">Are you sure?</p>
  <b>This action cannot be reversed!</b>

  <form action="?/deleteAllRecords" method="POST" class="mt-8 space-y-2" use:enhance={submitDelete}>
    <button type="submit" class="btn btn-error w-full text-white" disabled={loading}>
      Delete all sorting machine data
    </button>
  </form>
</Modal>
