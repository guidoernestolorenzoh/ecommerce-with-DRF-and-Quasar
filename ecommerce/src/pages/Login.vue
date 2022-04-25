<template>
  <div id="q-app">
    <q-layout view="lHh Lpr fff">
      <q-page
        class="window-height window-width row justify-center items-center"
        style="background: linear-gradient(#8274c5, #5a4a9f)"
      >
        <div class="column q-pa-lg">
          <div class="row">
            <q-card
              square
              class="shadow-24"
              style="width: 400px; height: 560px"
            >
              <q-card-section class="bg-deep-purple-7">
                <h4 class="text-h5 text-white q-my-md" align="center">{{ title }}</h4>
              </q-card-section>
              <q-card-section>
                <q-fab
                  color="primary"
                  @click="switchTypeForm"
                  icon="add"
                  class="absolute"
                  style="top: 0; right: 12px; transform: translateY(-50%)"
                >
                  <q-tooltip> Registro de nuevo usuario </q-tooltip>
                </q-fab>
                <q-form class="q-px-sm q-pt-xl" @submit.prevent="submit">
                  <q-input
                    ref="email"
                    square
                    clearable
                    v-model="email"
                    type="email"
                    lazy-rules
                    :rules="[this.required, this.isEmail, this.short]"
                    label="Email"
                  >
                    <template v-slot:prepend>
                      <q-icon name="email" />
                    </template>
                  </q-input>
                  <q-input
                    ref="username"
                    v-if="register"
                    square
                    clearable
                    v-model="username"
                    lazy-rules
                    :rules="[this.required, this.short]"
                    type="username"
                    label="Username"
                  >
                    <template v-slot:prepend>
                      <q-icon name="person" />
                    </template>
                  </q-input>
                  <q-input
                    ref="password"
                    square
                    clearable
                    v-model="password"
                    :type="passwordFieldType"
                    lazy-rules
                    :rules="[this.required, this.short]"
                    label="Password"
                  >
                    <template v-slot:prepend>
                      <q-icon name="lock" />
                    </template>
                    <template v-slot:append>
                      <q-icon
                        :name="visibilityIcon"
                        @click="switchVisibility"
                        class="cursor-pointer"
                      />
                    </template>
                  </q-input>
                  <q-input
                    ref="repassword"
                    v-if="register"
                    square
                    clearable
                    v-model="repassword"
                    :type="passwordFieldType"
                    lazy-rules
                    :rules="[this.required, this.short, this.diffPassword]"
                    label="Repita la contraseña"
                  >
                    <template v-slot:prepend>
                      <q-icon name="lock" />
                    </template>
                    <template v-slot:append>
                      <q-icon
                        :name="visibilityIcon"
                        @click="switchVisibility"
                        class="cursor-pointer"
                      />
                    </template>
                  </q-input>
                </q-form>
              </q-card-section>

              <q-card-actions class="q-px-lg">
                <q-btn 
                    type="submit"
                    rounded
                    unelevated
                    size="lg"
                    color="secondary"
                    @click="submit"
                    class="full-width text-white"
                    :label="btnLabel"
                />
              </q-card-actions>
              <q-card-section v-if="!register" class="text-center q-pa-sm">
                <p class="text-grey-6">Olvidó la contraseña?</p>
              </q-card-section>
            </q-card>
          </div>
        </div>
      </q-page>
    </q-layout>
  </div>
</template>

<script>
import { useQuasar } from 'quasar'
let $q

export default {
  name: "LogIn",
  data() {
    return {
        title: 'Login',
        email: '',
        username: '',
        password: '',
        repassword: '',
        register: false,
        passwordFieldType: 'password',
        btnLabel: 'Login',
        visibility: false,
        visibilityIcon: 'visibility'
    };
  },
  methods: {
      required (val) {
      return  (val && val.length > 0 || 'El campo no debe estar vacío')
    },
     diffPassword (val) {
       const val2 = this.$refs.password.value
       return (val && (val===val2) || 'La contraseña no coincide!')
     },
     short(val) {
      return  (val && val.length > 3 || 'La contraseña es demasiado corta')
    },
     isEmail (val) {
       const emailPattern = /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/
       return (emailPattern.test(val) || 'Ingrese un email correcto')
     },
     submit () {
       if (this.register){
          this.$refs.email.validate()
          this.$refs.username.validate()
          this.$refs.password.validate()
          this.$refs.repassword.validate()
       } else {
          this.$refs.email.validate()
          this.$refs.password.validate()      
       }
      
       if (!this.register) 
         if (!this.$refs.email.hasError && (!this.$refs.password.hasError))
     {
       this.$q.notify({
          icon: 'done',
          color: 'positive',
          message: 'Autorizado'
        })
     }
     },
     switchTypeForm(){ 
       this.register = !this.register
       this.title = this.register ? 'Nuevo Usuario' : 'Login'
       this.btnLabel = this.register ? 'Registrar' : 'Login'
     },
    switchVisibility() {
      this.visibility = !this.visibility
      this.passwordFieldType = this.visibility ? 'text' : 'password'
      this.visibilityIcon =  this.visibility ? 'visibility_off' : 'visibility'
    }  
  },
  mounted() {
      $q = useQuasar()
  },
};
</script>

<style scoped>
.wave {
  position: fixed;
  height: 100%;
  left: 0;
  bottom: 0;
  z-index: -1;
}
</style>