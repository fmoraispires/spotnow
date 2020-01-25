<template>
  <div>
    <div class="container">
     <div class="intro-text">
          <!-- titulo-->
          <div class="intro-heading text-uppercase">Adicione a sua Garagem</div>
          <div class="intro-lead-in">Registe a sua garagem</div>
        <b-card>
           <b-card-text>Insira os dados da sua garagem</b-card-text>
        <b-form @submit="saveGarage" @reset="onReset">
          <b-form-group id="input-group-1">
            <label class="label" for="input-1">Localização:</label>
            <b-form-input
              class="input"
              id="input-1"
              v-model="form.morada"
              type="text"
              required
              placeholder="Morada"
            ></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-2">
            <label class="label" for="input-2">Valor:</label>
            <b-form-input
              class="input"
              id="input-2"
              v-model="form.valor"
              type="text"
              required
              placeholder="valor"
            ></b-form-input>
            </b-form-group>
            <b-row>
               <b-form-group id="input-group-3">
            <label class="label" for="input-3">Horário de Inicio:</label>
            <b-form-input
              class="input"
              id="input-3"
              v-model="form.time1"
              type="time"
              required
              placeholder="inicio"
            ></b-form-input>
            </b-form-group>
             <b-form-group id="input-group-4">
            <label class="label" for="input-4">Horário de Fim:</label>
            <b-form-input
              class="input"
              id="input-4"
              v-model="form.time2"
              type="time"
              required
              placeholder="fim"
            ></b-form-input>
            </b-form-group>
            </b-row>
           
            <b-form-file
              v-model="file"
              :state="Boolean(file)"
              placeholder="Choose a file or drop it here..."
              drop-placeholder="Drop file here..."
            ></b-form-file>
            <div class="mt-3">Selected file: {{ file ? file.name : '' }}</div>

            <!-- Plain mode -->
            <b-form-file v-model="file2" class="mt-3" plain></b-form-file>
            <div class="mt-3">Selected file: {{ file2 ? file2.name : '' }}</div>
          

          <b-row>
            <b-col sm="2">
              <label for="Observações">Observações:</label>
            </b-col>
            <b-col sm="10">
              <b-form-textarea id="textarea-small" size="sm" placeholder="outras observações"></b-form-textarea>
            </b-col>
          </b-row>

          <b-button type="submit" variant="primary" @click="handleSubmit">Guardar</b-button>
          <b-button type="reset" variant="danger">Editar</b-button>
        </b-form>
        </b-card>
        </div>
    </div>  
  </div>
</template>
<script>
export default {
  name: "AddGarage",
  data() {
    return {
      file: null,
      file2: null,
      form: {
        morada: "",
        valor: ""
      }
    };
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      alert(JSON.stringify(this.form));

      if (
        this.password === this.password_confirmation &&
        this.password.length > 0
      ) {
        let url = "http://localhost:3000/register"; //substituir pelo url da api
        //if(this.is_admin != null || this.is_admin == 1) url = "http://localhost:3000/register-admin"
        this.$http
          .post(url, {
            email: this.form.email,
            name: this.form.name,
            password: this.form.pass,
            address: this.form.address,
            nif: this.form.nif,
            tlm: this.form.tlm,
          })
          .then(response => {
            localStorage.setItem("user", JSON.stringify(response.data.user));
            localStorage.setItem("jwt", response.data.token);

            if (localStorage.getItem("jwt") != null) {
              this.$emit("loggedIn");
              if (this.$route.params.nextUrl != null) {
                this.$router.push(this.$route.params.nextUrl);
              } else {
                this.$router.push("/");
              }
            }
          });
        // .catch(error => {
        //     //console.error(error);
        // });
      } else {
        this.password = "";
        this.passwordConfirm = "";
        return alert("Passwords do not match");
      }
    }
  }
};
</script>


<style scoped>
.intro-text{
    padding-top: 10px;
    padding-bottom: 100px;
}

.intro-text .intro-lead-in {
    
    font-size: 22px;
    font-style: italic;
    line-height: 22px;
    margin-bottom: 25px;
    font-family: 'Montserrat', 'Helvetica Neue', Helvetica, sans-serif;
}

.intro-text .intro-heading {
    font-size: 50px;
    font-weight: 700;
    line-height: 50px;
    margin-bottom: 25px;
    font-family: 'Montserrat', 'Helvetica Neue', Helvetica, sans-serif;
}

.form{
  height: 100%;
  margin-left: 100px;
  margin-right: 100px;
  margin-top: 25px;
}

.label{
  float: left ;
  width:30%;
}
.input{
  max-width: 70%;
}

</style>