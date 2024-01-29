<script>
  import '../app.pcss';
  import { Icon } from '@steeze-ui/svelte-icon';
  import { ChartBar, Cog6Tooth, Squares2x2 } from '@steeze-ui/heroicons';
  import { Sidebar, SidebarLink, SidebarHeading } from '$lib/components';

  export let data;

  let modules = [];
  data.modules.forEach((module) => {
    modules.push(module.name);
  });
</script>

<div class="drawer bg-base-100 lg:drawer-open">
  <!-- Invisible sidebar toggle -->
  <input id="drawer" type="checkbox" class="drawer-toggle" />

  <div class="drawer-content">
    <!-- Navbar -->
    <div
      class="
  bg-primary text-base-content sticky top-0 z-30 flex h-16 w-full justify-center text-white backdrop-blur transition-all duration-100 [transform:translate3d(0,0,0)]
  
  "
    >
      <nav class="navbar w-full">
        <div class="flex flex-1 md:gap-1 lg:gap-2">
          <span class="tooltip tooltip-bottom before:text-xs before:content-[attr(data-tip)]">
            <label
              aria-label="Open menu"
              for="drawer"
              class="} btn btn-square btn-ghost drawer-button lg:hidden"
            >
              <svg
                width="20"
                height="20"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                class="inline-block h-5 w-5 stroke-current md:h-6 md:w-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 6h16M4 12h16M4 18h16"
                />
              </svg>
            </label>
          </span>
          <div class="flex items-center gap-2 lg:hidden">
            <a
              href="/"
              aria-current="page"
              aria-label="Homepage"
              class="flex-0 btn btn-ghost gap-1 px-2 md:gap-2"
              data-svelte-h="svelte-11qcss2"
            >
              <div class="font-title inline-flex text-lg normal-case md:text-2xl">
                <span>Dashboard</span>
              </div>
            </a>
          </div>
        </div>
        <div class="items-end">
          <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
          <!-- svelte-ignore a11y-label-has-associated-control -->
          <div class="dropdown dropdown-end">
            <label tabindex="0" class="avatar btn btn-circle btn-ghost">
              <div class="w-10 rounded-full">
                <img
                  src={`https://ui-avatars.com/api/?name=${data.user?.name}`}
                  alt="Profielfoto"
                />
              </div>
            </label>
            <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
            <ul
              tabindex="0"
              class="menu-compact menu dropdown-content rounded-box bg-base-100 mt-3 w-52 p-2 text-black shadow"
            >
              <li>
                <form action="/logout" method="POST">
                  <button>Uitloggen</button>
                </form>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>

    <!-- Page content -->
    <div class="py-10">
      <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
        <slot />
      </div>
    </div>
  </div>

  <!-- Sidebar -->
  <div class="drawer-side z-40" style="scroll-behavior: smooth; scroll-padding-top: 5rem;">
    <label for="drawer" class="drawer-overlay" aria-label="Close menu" />

    <Sidebar>
      <ul class="lg:menu-md space-y-1 py-0 text-[#abb0c2]">
        {#if modules.includes('Sorting machine')}
          <SidebarHeading title="Sorting Machine" />
          <SidebarLink title="Statistics" href="/sorting-machine/statistics">
            <Icon slot="icon" src={ChartBar} size="1rem" class="mr-2" />
          </SidebarLink>
          <SidebarLink title="Settings" href="/sorting-machine/settings">
            <Icon slot="icon" src={Cog6Tooth} size="1rem" class="mr-2" />
          </SidebarLink>
        {/if}

        <SidebarHeading title="System" />
        <SidebarLink title="Modules" href="/system/modules">
          <Icon slot="icon" src={Squares2x2} size="1rem" class="mr-2" />
        </SidebarLink>
      </ul>
    </Sidebar>
  </div>
</div>
