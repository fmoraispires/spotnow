 <template>
  <div>
    <div class="container">
      <div class="intro-text">
        <div class="intro-heading text-uppercase">Bem-Vindo</div>
        <div
          class="intro-lead-in"
        >Crie a sua conta, junte-se a nós e passe a usufruir do nosso serviço</div>

        <v-card flat tile class="card">
          <form class="form">
            <div class="card-title">
              <b>Introduza os seus dados</b>
            </div>
            <v-text-field
              class="input"
              v-model="email"
              :error-messages="emailErrors"
              label="E-mail"
              required
              filled
              rounded
              @input="$v.email.$touch()"
              @blur="$v.email.$touch()"
              dense
            ></v-text-field>
            <v-text-field
              class="input"
              v-model="name"
              :error-messages="nameErrors"
              label="Nome de Utilizador"
              required
              @input="$v.nif.$touch()"
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
                <!-- <router-link to="/login"> -->
                <v-btn @click="handleSubmit" :disabled='!isComplete' depressed rounded x-large dark>
                  <b>Registe-se</b>
                  <v-icon class="icon">fas fa-arrow-right</v-icon>
                </v-btn>
                <!-- </router-link> -->
              </div>
            </v-row>
             <v-alert
          :value="alert"
          type="success"
          dismissible
          transition="scale-transition"
        >Registo com sucesso</v-alert>
          </form>
        </v-card>
       
      </div>
    </div>
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
    nif: { required },
    tlm: { required },
    checkbox: {required,checked(val) {
        return val;
      }}
  },

  data() {
    return {
      alert: false,
      show1: false,
      name: "",
      email: "",
      password: "",
      nif: "",
      tlm: "",
      checkbox: null,
      rules: {
        required: value => !!value || "Campo Obrigatório.",
        min: v => v.length >= 2 || "Minimo 2 caracteres."
      }
    };
  },

  computed: {
  
  isComplete () {
    return this.name && this.password && this.email && this.nif && this.tlm && this.checkbox;
  },
    checkboxErrors() {
      const errors = [];
      if (!this.$v.checkbox.$dirty) return errors;
      !this.$v.checkbox.checked &&
        errors.push("Para se registar é preciso aceitar os termos e condições");
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
    handleSubmit() {
      this.submit();
      this.isSignUP();
    },

    submit(){
      this.$http
        .post(
          "http://spotnow.westeurope.cloudapp.azure.com:8000/api/client-add/",
          {
            "user": {
              "username": this.name,
              "password": this.password,
              "email": this.email
            },
            "nif": this.nif,
            "telephone": this.tlm
          }
        )
        .then(response => console.log(response));
      // }
      /* eslint-enable no-console */
    },
    isSignUP(){
      this.alert = true;
    return this.alert;
  },
  }
};
</script>
<style scoped>
.intro-text {
  padding-top: 10px;
  padding-bottom: 100px;
  margin: auto;
}
.intro-lead-in {
  font-size: 22px;
  font-style: italic;
  line-height: 22px;
  margin: auto;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}
.intro-heading {
  font-size: 50px;
  font-weight: bold;
  line-height: 50px;
  margin: auto;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}
.card {
  height: 850px;
  width: 600px;
  margin: auto;
}

.card-title {
  padding-top: 20px;
  padding-bottom: 30px;
  font-size: 22px;
  font-style: italic;
  line-height: 22px;
  margin: auto;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}
.form {
  justify-content: center;
  margin: auto;
}

.input {
  margin: auto;
  padding-bottom: 25px;
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
  padding-bottom: 15px;
}

.input2 {
  margin: auto;
  max-width: 100%;
  max-height: 25%;
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
</style>