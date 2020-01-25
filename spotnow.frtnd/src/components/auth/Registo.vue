 <template>
  <div>
    <div class="container">
      <div class="intro-text">
        <div class="intro-heading text-uppercase">Bem-Vindo</div>
        <div
          class="intro-lead-in"
        >Crie a sua conta, junte-se a nós e passe a usufruir do nosso serviço</div>
        <b-card class="form">
          <b-card-text>Introduza os seus dados</b-card-text>
          <b-form @submit="onSubmit" @reset="onReset" >
            <b-form-group id="input-group-1">
              <label class="label" for="input-1">E-mail:</label>
              <b-form-input
                class="input"
                id="input-1"
                v-model="form.email"
                type="email"
                required
                placeholder="E-mail"
              ></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-2">
              <label class="label" for="input-2">Nome de Utilizador:</label>
              <b-form-input
                class="input"
                id="input-2"
                v-model="form.name"
                required
                placeholder="Nome de Utilizador"
              ></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-3">
              <label class="label" for="input-3">Palavra-Passe:</label>
              <b-form-input
                class="input"
                id="input-3"
                v-model="form.pass"
                type="password"
                required
                placeholder="Introduza a sua Palavra-Passe"
              ></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-4">
              <label class="label" for="input-4">Confime a sua Palavra-Passe:</label>
              <b-form-input
                class="input"
                id="input-4"
                v-model="form.confim"
                type="password"
                required
                placeholder="Confime a sua Palavra-Passe"
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-5">
              <label class="label" for="input-5">Morada:</label>
              <b-form-input
                class="input"
                id="input-5"
                v-model="form.address"
                required
                placeholder="Morada"
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-6">
              <label class="label" for="input-6">Número de Identificação Fiscal (NIF):</label>
              <b-form-input
                class="input"
                id="input-6"
                v-model="form.nif"
                type="tel"
                required
                placeholder="Número de Identificação Fiscal (NIF)"
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-7">
              <label class="label" for="input-7">Telemóvel:</label>
              <b-form-input
                class="input"
                id="input-7"
                v-model="form.tlm"
                type="tel"
                pattern="[0-9]{3}-[0-9]{3}-[0-9]{3}"
                required
                placeholder="Telemóvel"
              ></b-form-input>
              <small>Formato: 123-456-789</small>
            </b-form-group>


            <b-form-group id="input-group-7">
              <b-form-checkbox-group v-model="form.checked" id="checkboxes-4">
                <b-form-checkbox value="me">Aceito os termos e condições</b-form-checkbox>
              </b-form-checkbox-group>
            </b-form-group>

            <b-button type="submit"  dark @click="handleSubmit">Submeter</b-button>
            <b-button type="reset" variant="danger">Limpar Dados</b-button>
          </b-form>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
// email, username, password, NIF, telemovel
export default {
  name: "Registo",
  data() {
    return {
      form: {
        email: "",
        name: "",
        pass: "",
        confirm: "",
        address: "",
        nif: "",
        tlm: "",
        checked: []
      },
    };
  },
  methods: {
     /* eslint-disable no-console */
    handleSubmit(e) {
      e.preventDefault();

        
        this.$http
          .post("http://spotnow.westeurope.cloudapp.azure.com:8000/api/owner-add/", 
          {
            "user": {
            "username": this.form.name,
            "password": this.form.pass,
            "email": this.form.email
          },
          "nif": this.form.nif,
          "telephone": this.form.tlm
          })
          .then(response => console.log(response));
      }
  }
    /* eslint-enable no-console */
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
  margin-bottom: 15px;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}

.form {
  height: 100%;
  margin-left: 100px;
  margin-right: 100px;
  margin-bottom: 50px;
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