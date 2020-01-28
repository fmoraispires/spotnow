<template>
  <div>
    <div class="container">
      <div class="intro-text">
        <!-- titulo-->
        <div class="intro-heading text-uppercase">Histórico</div>
        <div class="intro-lead-in">As garagens que você já visitou</div>
      </div>
    </div>
    <v-container>
      <v-row dense>
        <v-col v-for="(item, i) in items" :key="i" cols="12">
          <v-card :color="item.color" dark>
            <div class="d-flex flex-no-wrap justify-space-between">
                   <v-avatar class="ma-3" size="125" tile>
                  <v-img :src="item.src"></v-img>
                </v-avatar>
              <div>
                <v-card-title class="headline" v-text="item.title"></v-card-title>
                <v-card-subtitle v-text="item.artist"></v-card-subtitle>
              </div>
              <v-card-actions align-items="center left">
                <v-btn text>Reservar</v-btn>

                <v-btn color="red" text>Eliminar</v-btn>

                <v-spacer></v-spacer>

                <v-btn icon @click="show = !show" down> 
                  <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                </v-btn>
              </v-card-actions>

              <v-expand-transition down>
                <div v-show="show">
                  <v-divider></v-divider>

                  <v-card-text>I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.</v-card-text>
                </div>
              </v-expand-transition>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Historic",

  data: () => ({
    items: [
      {
        color: "#1F7087",
        src: "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
        title: "Supermodel",
        artist: "Foster the People"
      },
      {
        color: "#952175",
        src: "https://cdn.vuetifyjs.com/images/cards/halcyon.png",
        title: "Halcyon Days",
        artist: "Ellie Goulding"
      }
    ],
    show: false,
  })
};
</script>

<style>
.intro-text {
  padding-top: 10px;
  padding-bottom: 80px;
}

.intro-text .intro-lead-in {
  font-size: 22px;
  font-style: italic;
  line-height: 22px;
  margin-bottom: 25px;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}

.intro-text .intro-heading {
  font-size: 50px;
  font-weight: 700;
  line-height: 50px;
  margin-bottom: 15px;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}
</style>