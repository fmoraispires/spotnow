<template>
  <v-footer dark padless>
    <v-card width="100%">
      <v-row >
        <v-card-text>
          <a href="https://www.facebook.com/SpotNow-110913667105487/" target="_blank">
          <v-btn  class="mx-4 white--text" icon>
            <v-icon size="24px">fab fa-facebook</v-icon>
          </v-btn>
          </a>
          <a href="https://aboutme.google.com/u/0/?referer=gplus" target="_blank">
           <v-btn  class="mx-4 white--text" icon>
            <v-icon size="24px">fab fa-google-plus</v-icon>
          </v-btn>
          </a>
        </v-card-text>
      </v-row>
      <v-divider></v-divider>
      <v-row justify="center" no-gutters>
        <v-card-text>
          <router-link to="/">
            <v-btn color="white" text rounded class="my-2">Home</v-btn>
          </router-link>
          <router-link to="/about">
            <v-btn color="white" text rounded class="my-2">A Nossa História</v-btn>
          </router-link>
          <router-link to="/team">
            <v-btn color="white" text rounded class="my-2">A Equipa</v-btn>
          </router-link>
          <router-link to="/contact">
            <v-btn color="white" text rounded class="my-2">Contacte-nos</v-btn>
          </router-link>
        </v-card-text>
      </v-row>
      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} —
        <strong>SpotNow</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    icons: [ {
          icon:'fab fa-facebook',
        },{
          icon:'fab fa-google-plus',
        },]
  })
};
</script>

<style scoped>
.footer{
}
</style>