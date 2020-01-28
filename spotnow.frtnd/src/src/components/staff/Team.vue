<template>
  <div>
    <div class="container">
      <div class="intro-text">
        <!-- titulo-->
        <div class="intro-heading text-uppercase">A Equipa</div>
        <div class="intro-lead-in">Os elementos da Empresa</div>
      </div>
    </div>
    <v-container fluid>
      <v-row dense>
        <v-col v-for="card in cards" :key="card.title" :cols="card.flex">
          <v-card>
            <v-img
              :src="card.src"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="200px"
            >
              <v-card-title v-text="card.title"></v-card-title>
            </v-img>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn v-for="icon in icons" :key="icon" class="mx-4 blue--text" icon>
                <v-icon size="24px">{{ icon }}</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
  
<script>
export default {
  data: () => ({
    cards: [
      {
        title: "Bruno Nascimento",
        src: "https://cdn.vuetifyjs.com/images/cards/house.jpg",
        flex: 12
      },
      {
        title: "Bruno",
        src: "https://cdn.vuetifyjs.com/images/cards/road.jpg",
        flex: 6
      },
      {
        title: "Daniel",
        src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        flex: 6
      },
      {
        title: "Francisco",
        src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        flex: 6
      },
      {
        title: "Luis",
        src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        flex: 6
      },
      {
        title: "Miguel",
        src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        flex: 6
      },
      {
        title: "Norberto",
        src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        flex: 6
      },
      {
        title: "Rui",
        src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        flex: 6
      },
      {
        title: "Vitor",
        src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        flex: 6
      }
    ],
    icons: [
      "fab fa-facebook",
      "fab fa-twitter",
      "fab fa-google-plus",
      "fab fa-linkedin",
      "fab fa-instagram"
    ]
  })
};
</script>

<style scoped>
</style> 