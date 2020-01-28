<template>
  <div class="container">
    <div class="intro-text">
      <div class="intro-heading text-uppercase">Chegou ao seu Destino</div>
      <div class="intro-lead-in">Utilize os botões para interagir com a porta da garagem</div>
    </div>
    <!-- <v-card class="card"> -->
      <div class="fill-height">
        <v-btn dark  rounded x-large @click="OpenGarage" class="btn1"><v-icon size="50px">mdi-garage-open</v-icon><b>Abrir</b></v-btn>
        
        <v-btn dark x-large rounded  @click="CloseGarage" class="btn1"><v-icon size="50px">mdi-garage</v-icon><b>Fechar</b></v-btn>
      </div>
    <!-- </v-card> -->
  </div>
</template>

<script>
export default {
  name: "Door",
  data() {
    return {
      garage: null,
    }
  },
  methods: {
    /* eslint-disable no-console */
    OpenGarage(){
      this.garage = true;

      this.$http
          .post("http://spotnow.westeurope.cloudapp.azure.com:8000/api/smartlock-command/", 
            { "token":"2",
              "msg": "OPEN"})
          .then(response => console.log(response));


    },
    CloseGarage(){
      this.garage = false;
      this.$http
          .post("http://spotnow.westeurope.cloudapp.azure.com:8000/api/smartlock-command/", 
          { "token":"2",
            "msg": "CLOSE"})
          .then(response => console.log(response));

    }
  }
  /* eslint-enable no-console */
};
</script>

<style>
.container{
    align-items:center;
}
.intro-text {
  padding-top: 30px;
  padding-bottom: 30px;
}

.intro-lead-in {
  font-size: 22px;
  font-weight: bold;
  font-style: italic;
  line-height: 22px;
  margin:auto;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}
.intro-heading {
  font-size: 50px;
  font-weight: bold;
  line-height: 50px;
  margin:auto;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}
.card{
    height: 400px;
    width:300px;
    margin: auto;
    padding-top: 40px;
}

.fill-height{
  padding-top:150px;
  padding-bottom:150px;

}

.btn1{
    align-items: center;
    margin-left: 40px;
    padding-left: 40px;

}
</style>