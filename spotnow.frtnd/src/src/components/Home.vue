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
            >Crie a sua conta, junte-se a nós e rentabilize a sua garagem</div>
          </div>
        </div>
        <form class="form">
          <v-text-field
            class="input"
            v-model="email"
            :error-messages="emailErrors"
            label="E-mail"
            required
            @input="$v.email.$touch()"
            @blur="$v.email.$touch()"
            filled
            rounded
            dense
          ></v-text-field>
          <v-text-field
            class="input"
            v-model="name"
            :error-messages="nameErrors"
            label="Nome de Utilizador"
            required
            @input="$v.name.$touch()"
            @blur="$v.name.$touch()"
            filled
            rounded
            dense
          ></v-text-field>
          <v-text-field
            class="input"
            v-model="password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show1 ? 'text' : 'password'"
            label="Palavra-Passe"
            hint="At least 2 characters"
            counter
            @click:append="show1 = !show1"
            filled
            rounded
            dense
          ></v-text-field>
          <v-text-field
            v-model="nif"
            class="input"
            label="Número de Identificação Fiscal (NIF)"
            :error-messages="nifErrors"
            required
            @input="$v.nif.$touch()"
            @blur="$v.nif.$touch()"
            filled
            rounded
            dense
          ></v-text-field>
          <v-text-field
            class="input2"
            v-model="tlm"
            :error-messages="tlmErrors"
            label="Telemóvel"
            required
            @input="$v.tlm.$touch()"
            @blur="$v.tlm.$touch()"
            filled
            rounded
            dense
          ></v-text-field>
          <v-row class="terms">
            <v-checkbox
              v-model="checkbox"
              :error-messages="checkboxErrors"
              required
              @change="$v.checkbox.$touch()"
              @blur="$v.checkbox.$touch()"
            ></v-checkbox>
            <b>
              Li e aceito os
              <a href="http://default-template.wikidot.com/legal:terms-of-use">
                <b>Termos de Utilização</b>
              </a> do SpotNow.
            </b>
          </v-row>

          <v-row class="bot">
              <div class="bot2">
              <b>Tem uma conta?</b>
              <router-link to="/login">
                <a class="ancora">
                  <b>Iniciar Sessão</b>
                </a>
              </router-link>
            </div>
            <div class="signup">
              <v-btn @click="submit" depressed rounded x-large dark>
                <b>Registe-se</b>
                <v-icon class="icon">fas fa-arrow-right</v-icon>
              </v-btn>
            </div>
          </v-row>
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
import { validationMixin } from "vuelidate";
import { required, email } from "vuelidate/lib/validators";

export default {
  name: "Home",
  mixins: [validationMixin],
  validations: {
    name: { required },
    email: { required, email },
    password: { required },
    nif: { required },
    tlm: { required },

    checkbox: {
      checked(val) {
        return val;
      }
    }
  },

  data() {
    return {
      show1: false,
      name: "",
      email: "",
      password: "",
      nif: "",
      tlm: "",
      rules: {
        required: value => !!value || "Required.",
        min: v => v.length >= 2 || "Min 2 characters"
      },
    };
  },

  computed: {
    checkboxErrors() {
      const errors = [];
      if (!this.$v.checkbox.$dirty) return errors;
      !this.$v.checkbox.checked && errors.push("Para se registar é preciso aceitar os termos e condições");
      return errors;
    },
    nifErrors() {
      const errors = [];
      if (!this.$v.nif.$dirty) return errors;
      !this.$v.nif.required && errors.push("Campo obrigatório");
      return errors;
    },
    tlmErrors() {
      const errors = [];
      if (!this.$v.tlm.$dirty) return errors;
      !this.$v.tlm.required && errors.push("Campo obrigatório");
      return errors;
    },

    nameErrors() {
      const errors = [];
      if (!this.$v.name.$dirty) return errors;
      !this.$v.name.required && errors.push("Campo obrigatório");
      return errors;
    },
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push("Tem de ser um e-mail válido");
      !this.$v.email.required && errors.push("Campo obrigatório");
      return errors;
    }
  },

  methods: {
    /* eslint-disable no-console */
    submit() {
  
      this.$http
          .post("http://spotnow.westeurope.cloudapp.azure.com:8000/api/owner-add/", 
          {
            "user": {
            "username": this.name,
            "password": this.pass,
            "email": this.email
          },
          "nif": this.nif,
          "telephone": this.tlm
          })
          .then(response => console.log(response));
      // }
      /* eslint-enable no-console */
    }
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
  height: 1000px;
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
  height: 850px;
  width: 600px;
  margin: auto;
  padding:auto;
  top: 15px;
  align-content: center;
}
.form {
  justify-content: center;
  padding-top: 0px;
  margin: auto;
}
.input {
  margin: auto;
  padding-bottom: 25px;
  max-width: 100%;
  max-height: 25%;
}
.input2 {
  margin: auto;
  max-width: 100%;
  max-height: 25%;
}

.terms {
  align-items: center;
  margin-left: 10px;
  padding-top: 0px;
}
.signup {
  margin: auto;
  padding-top: 15px;
  padding-left: 30px;
}
.icon {
  margin-left: 5px;
}
.ancora {
  margin-left: 5px;
}

.bot2 {
  margin: auto;
}
.bot {
  align-items: center;
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