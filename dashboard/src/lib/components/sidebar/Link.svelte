<script>
  export let href;
  export let title;
</script>

<li class="flex flex-row gap-4 text-[#abb0c2] hover:bg-[#272b33]">
  <a {href} data-sveltekit-preload-data="hover">
    <span class="flex flex-row">
      <slot name="icon" />
      {title}
    </span>
  </a>
</li>
