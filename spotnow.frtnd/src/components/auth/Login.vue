 <template>
  <div>
    <div class="container">
      <div class="intro-text">
        <!-- titulo-->
        <div class="intro-heading text-uppercase">Bem-Vindo</div>
        <div class="intro-lead-in">Inicie Sessão e usufrua do serviço</div>
        <b-card class="form">
          <b-card-text>Introduza os seus dados</b-card-text>
          <b-form @submit="handleSubmit" @reset="onReset">
            <b-form-group id="input-group-1">
              <label class="label" for="input-1">Nome de Utilizador:</label>
              <b-form-input
                class="input"
                id="input-1"
                v-model="form.name"
                type="text"
                required
                placeholder="Nome de Utilizador"
              ></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-2">
              <label class="label" for="input-1">Palavra-Passe:</label>
              <b-form-input
                class="input"
                id="input-2"
                v-model="form.pass"
                type="password"
                required
                placeholder="Palavra-Passe"
              ></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-3">
              <b-form-checkbox-group v-model="form.checked" id="checkboxes-4">
                <b-form-checkbox value="me">Manter-me ligado</b-form-checkbox>
              </b-form-checkbox-group>
            </b-form-group>

            <b-button
              type="submit"
              dark
              icon="fas fa-sign-in-alt"
              @click="handleSubmit"
            >Iniciar Sessão</b-button>
            <b-button type="reset" variant="danger">Esqueci-me</b-button>
          </b-form>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      form: {
        name: "",
        pass: "",
        checked: []
      }
    };
  },
  methods: {
    /* eslint-disable no-console */
    handleSubmit(evt) {
      evt.preventDefault();
      if (this.form.name != "" && this.form.pass != "") {
        this.$http
          .post(
            "http://spotnow.westeurope.cloudapp.azure.com:8000/rest-auth/login/",
            {
              username: this.form.name,
              email: "",
              password: this.form.pass
            }
          )
          .then(response => console.log(response))
          .finally(console.log("ola"));
      }
    },
    /* eslint-enable no-console */

    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.name = "";
      this.form.pass = "";
      this.form.checked = [];
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>

<style scoped>
.intro-text {
  padding-top: 10px;
  padding-bottom: 100px;
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
  margin-bottom: 25px;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}

.form {
  height: 300px;
  margin-left: 100px;
  margin-right: 100px;
  margin-top: 25px;
}

.label {
  float: left;
  width: 30%;
}
.input {
  max-width: 70%;
}
</style>