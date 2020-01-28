 <template>
  <div>
    <div class="container">
      <div class="intro-text">
        <div class="intro-heading text-uppercase">Bem-Vindo</div>
        <div class="intro-lead-in">Inicie Sessão e usufrua do serviço</div>
        <v-card flat tile class="cardlogin">
          <form class="form">
            <div class="card-title">
              <b>Introduza os seus dados</b>
            </div>
            <v-text-field
            class="input"
            v-model="name"
            :error-messages="nameErrors"
            label="Nome de Utilizador"
            required
            @blur="$v.name.$touch()"
            filled
            rounded
            dense
          ></v-text-field>
            <v-text-field
              class="input2"
              v-model="password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :rules="[rules.required, rules.min]"
              :type="show1 ? 'text' : 'password'"
              label="Palavra-Passe"
              hint="At least 2 characters"
              @click:append="show1 = !show1"
              filled
              rounded
              dense
            ></v-text-field>
              <div class="bot2">
                <b>Não tem uma conta?</b>
                <router-link to="/registo">
                  <a class="ancora">
                    <b>Registe-se aqui</b>
                  </a>
                </router-link>
              </div>
              <div class="signup">
                <v-btn @click="submit" depressed rounded large dark>
                  <b>Iniciar Sessão</b>
                  <v-icon class="icon">fas fa-sign-in-alt</v-icon>
                </v-btn>
              </div>
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

    checkbox: {
      checked(val) {
        return val;
      }
    }
  },

  data() {
    return {
      show1: false,
      email: "",
      password: "",

      rules: {
        required: value => !!value || "Campo Obrigatório.",
        min: v => v.length >= 2 || "Minimo 2 caracteres."
      }
    };
  },

  computed: {
     nameErrors() {
      const errors = [];
      if (!this.$v.name.$dirty) return errors;
      !this.$v.name.required && errors.push("Campo obrigatório");
      return errors;
    },
  },

  methods: {
    /* eslint-disable no-console */
    submit() {
     this.$http
          .post(
            "http://spotnow.westeurope.cloudapp.azure.com:8000/rest-auth/login/",
            {
              "username": this.username,
              "email": this.email,
              "password": this.password
            }
          )
        .then(response => console.log(response));
      // }
      /* eslint-enable no-console */
    }
  }
};
</script>
<style scoped>
.intro-text {
  padding-top: 10px;
  padding-bottom: 100px;
  margin:auto;
}

 .intro-lead-in {
  font-size: 22px;
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

.cardlogin {
  margin: auto;
  height: 400px;
  width:800px;
}

.card-title {
  padding-top:50px;
  padding-bottom:30px;
  font-size: 22px;
  font-style: italic;
  line-height: 22px;
  margin: auto;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}
.form {
  justify-content: center;
  margin:auto;
}
.input {
  margin: auto;
  padding-bottom: 25px;
  max-width: 60%;
  max-height: 25%;
}

.input2 {
  margin: auto;
  max-width: 60%;
  max-height: 25%;
}

.signup {
margin: auto;
padding-top: 15px;
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