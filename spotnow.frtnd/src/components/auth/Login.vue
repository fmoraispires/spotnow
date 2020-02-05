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
                <v-btn @click="login" :disabled='!isComplete' depressed rounded x-large dark>
                  <b>Iniciar Sessão</b>
                  <v-icon class="icon">fas fa-sign-in-alt</v-icon>
                </v-btn>
              </div>
               <v-alert
          :value="alert"
          type="success"
          dismissible
          transition="scale-transition"
        >Login efectuado</v-alert>
          </form>
        </v-card>
      </div>
    </div>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, email} from "vuelidate/lib/validators";

export default {
  name: "Home",
  mixins: [validationMixin],
  validations: {
    email: { required,email },
  },

  data() {
    return {
      alert: false,
      email: "",
      name:"",
      password: "",
      rules: {
        required: value => !!value || "Campo Obrigatório.",
        min: v => v.length >= 2 || "Minimo 2 caracteres."
      }
    };
  },

  computed: {
    isComplete () {
    return this.email && this.password;
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
      this.login();
      this.isSignIn();
    },
    login() {
      
         let email = this.email
         let password = this.password
        this.$store.dispatch('login', {email, password}) 
       .then(() => this.$router.push('/'))
       .catch(err => console.log(err))
      }
      /* eslint-enable no-console */
    
  },
  isSignIn(){
      this.alert = true;
    return this.alert;
  },
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