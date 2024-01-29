<script>
  export let label;
  export let checked;
</script>

<label for={label}> <slot name="trigger" /></label>

<input type="checkbox" id={label} class="modal-toggle" {checked} />
<label for={label} class="modal modal-bottom sm:modal-middle">
  <label class="modal-box">
    <div class="text-center text-xl font-bold">
      <slot name="heading" />
    </div>
    <div class="my-2">
      <slot />
    </div>
    <div class="modal-action justify-center">
      <slot name="actions" />
    </div>
  </label>
</label>
