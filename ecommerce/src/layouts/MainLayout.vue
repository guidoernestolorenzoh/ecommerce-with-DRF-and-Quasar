<template>
  <div class="q-pa-lg-sm">
    <q-layout view="hHh lpR fFf">
      <q-header class="bg-blue">
        <q-toolbar>
          <q-btn flat @click="miniState = !miniState" round dense icon="menu" />
          <q-toolbar-title class="absolute-center">Ecommerce</q-toolbar-title>
        </q-toolbar>
      </q-header>

      <q-footer class="bg-blue">
        <q-tabs>
          <q-route-tab
            v-for="nav in navs"
            :key="nav.label"
            :to="nav.to" :icon="nav.icon" :label="nav.label"
          />
        </q-tabs>
      </q-footer>

<!--mini-to-overlay-->
      <q-drawer
        v-model="drawer"
        show-if-above

        :mini="miniState"

        :width="210"
        :breakpoint="767"
        bordered
        class="bg-grey-2"
      >
        <q-scroll-area class="fit">
          <q-list>
            <q-item-label header class="text-blue">Navigation</q-item-label>
            <q-item
              class="border-navig"
              :key="nav.label"
              v-for="nav in navs" :to="nav.to"
              clickable v-ripple exact
              active-class="my-menu-link"
            >
              <q-item-section avatar>
                <q-icon :name="nav.icon" />
              </q-item-section>

              <q-item-section>
                <q-item-label>{{ nav.label }}</q-item-label>
              </q-item-section>
            </q-item>

          </q-list>
        </q-scroll-area>
      </q-drawer>

      <q-page-container class="center">
        <q-page padding>
          <router-view />
        </q-page>
      </q-page-container>
    </q-layout>
  </div>
</template>


<script>
import { defineComponent, ref } from 'vue'
// import EssentialLink from 'components/EssentialLink.vue'
import axios from "axios";

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";


export default defineComponent({
  name: 'MainLayout',

  components: {
    // EssentialLink
  },

  setup () {
    const leftDrawerOpen = ref(false)

    return {
      drawer: ref(true),
      miniState: ref(false),

      navs: [
        {
          label: 'Unidad de Medida',
          icon: 'square_foot',
          to: '/measure-unit',
        },
        {
          label: 'Categoria de Productos',
          icon: 'category',
          to: '/category-product',
        },
        {
          label: 'Settings',
          icon: 'settings',
          to: '/settings',
        }
      ],


      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }

  }
})
</script>

<style lang="scss">
.my-menu-link{
  color: white;
  background: #5b8ef1;
}

.floating-button-add{
  margin: 35px 25px;
  top: 60px;
  font-size: 23px;
}
</style>
