<template>
  <div>
    <header class="masthead">
      <!-- Imagem principal e botaão de inscrição na Conferencia-->
        
      <v-card flat tile class="card">
        <div class="container">
          <div class="intro-text">
            <div class="intro-heading text-uppercase">Bem-Vindo</div>
            <div
              class="intro-lead-in"
            >Crie a sua conta, junte-se a nós e passe a usufruir do nosso serviço</div>
          </div>
        </div>
        <form class="form">
          <v-text-field class="input"
            label="E-mail"
            filled
            rounded
            solo
          ></v-text-field>
          <v-text-field class="input"
            label="Nome de Utilizador"
            filled
            rounded
            solo
          ></v-text-field>
          <v-text-field class="input"
            label="Palavra-Passe"
            
             filled
            rounded
            solo
          ></v-text-field>
              <v-text-field class="input"
          label="Confirme a sua Palavra-Passe"
        filled
            rounded
            solo
          ></v-text-field>
            <v-text-field class="input"
            label="Número de Identificação Fiscal (NIF):"
             filled
            rounded
            solo
          ></v-text-field>


          <v-text-field class="input"
          label="Telemóvel"
            filled
            rounded
            solo
          ></v-text-field>
          <div>Li e aceito os <a href="http://default-template.wikidot.com/legal:terms-of-use">Termos de Utilização</a> do SpotNow.</div>

          <v-btn class="button-re" depressed  rounded large dark><b>Registe-se</b></v-btn>
  
        </form>
      </v-card>
    </header>
    <section id="why us">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2 class="section-heading text-uppercase">
              <b>conceito</b>
            </h2>
            <h3 class="section-subheading">
              <b>Explicar conceito</b>
            </h3>
          </div>
          <v-row>
            <v-card class="mx-auto" max-width="400">
              <v-img
                class="white--text align-end"
                height="200px"
                src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
              >
                <v-card-title>Top 10 Australian beaches</v-card-title>
              </v-img>

              <v-card-subtitle class="pb-0">Number 10</v-card-subtitle>

              <v-card-text class="text--primary">
                <div>Whitehaven Beach</div>

                <div>Whitsunday Island, Whitsunday Islands</div>
              </v-card-text>
            </v-card>
            <v-card class="mx-auto" max-width="400">
              <v-img
                class="white--text align-end"
                height="200px"
                src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
              >
                <v-card-title>Top 10 Australian beaches</v-card-title>
              </v-img>

              <v-card-subtitle class="pb-0">Number 10</v-card-subtitle>

              <v-card-text class="text--primary">
                <div>Whitehaven Beach</div>

                <div>Whitsunday Island, Whitsunday Islands</div>
              </v-card-text>
            </v-card>
          </v-row>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      items: [
        {
          title: "Rentabilize a sua Garagem",
          text: "Ganhe dinheiro connosco",
          text_btn: "Juntes-se a nós",
          src:
            "https://cdn.pixabay.com/photo/2017/08/11/14/16/garage-doors-2631247_960_720.jpg"
        },
        {
          title: "Não perca tempo",
          text: "Estacione connosco",
          text_btn: "Juntes-se a nós",
          src:
            "https://images.unsplash.com/40/x6YzbWWRq2sRhAacMjnl_Bangkok%20Indra%20market.jpg?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=967&q=80"
        }
      ],
      dialog: false
    };
  }
};
</script>

<style scoped>
header.masthead {
  color: black;
  background-image: url("https://cdn.pixabay.com/photo/2017/08/11/14/16/garage-doors-2631247_960_720.jpg");
  background-repeat: no-repeat;
  background-attachment: scroll;
  background-position: center center;
  background-size: cover;
  height: 785px;

}

.intro-text {
  padding-top: 0px;
  padding-bottom: 5px;
}

.intro-lead-in {
  font-size: 22px;
  font-weight: bold;
  font-style: italic;
  line-height: 22px;
  margin-top: 15px;
  margin-bottom: 5px;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}
.intro-heading {
  font-size: 50px;
  font-weight: bold;
  line-height: 50px;
  margin-top: 15px;
  margin-bottom: 5px;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}

.card {
  height: 785px;
  width: 600px;
  margin-left: 1000px;
  top: 0px;
  align-content:center;
  
}
.form{
    justify-content: center;
    margin-right:25px;
    margin-left:70px;

}
.button-re{
  justify:left;
}

.input {
  max-width: 90%;
  max-height:25%;
}

section {
  padding: 100px 0;
  background-color: lightgrey;
}

section h2.section-heading {
  font-size: 40px;
  margin-top: 0;
  margin-bottom: 15px;
}

section h3.section-subheading {
  font-size: 16px;
  font-weight: 400;
  font-style: italic;
  margin-bottom: 75px;
  text-transform: none;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}
</style>