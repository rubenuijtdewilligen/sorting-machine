<script>
  export let data;

  let modules = [];

  data.modules.forEach((module) => {
    modules.push(module.name);
  });

  const toggle = async (moduleName) => {
    console.log('hoi');
  };
</script>

<h3 class="title mb-2 text-2xl font-bold">Modules</h3>

<div class="form-control max-w-fit">
  <label class="label cursor-pointer">
    <span class="label-text">Sorting machine</span>
    <input
      type="checkbox"
      class="toggle toggle-primary ml-3"
      checked={modules.includes('Sorting machine')}
      on:change={async () => {
        await fetch('/api/toggleModule', {
          method: 'POST',
          body: JSON.stringify({ moduleName: 'Sorting machine' }),
          headers: {
            'content-type': 'application/json'
          }
        });
      }}
    />
  </label>
</div>
