<template>
  <div>
    <div class="container">
      <div class="intro-text">
        <!-- titulo-->
        <div class="intro-heading text-uppercase">Adicione a sua Garagem</div>
        <div class="intro-lead-in">Registe a sua garagem</div>
        <v-card flat tile class="card">
          <form class="form">
            <div class="card-title">
              <b>Insira os dados da smartlock da sua garagem</b>
            </div>
             <v-text-field
              class="input"
              v-model="name"
              :error-messages="nameErrors"
              label="Nome"
              required
              @input="$v.name.$touch()"
              @blur="$v.name.$touch()"
              filled
              rounded
              dense
            ></v-text-field>
            <v-text-field
              class="input"
              v-model="address"
              :error-messages="addressErrors"
              label="Morada"
              required
              @input="$v.address.$touch()"
              @blur="$v.address.$touch()"
              filled
              rounded
              dense
            ></v-text-field>
             <v-text-field
              class="input"
              v-model="city"
              :error-messages="cityErrors"
              label="Cidade"
              required
              @input="$v.city.$touch()"
              @blur="$v.city.$touch()"
              filled
              rounded
              dense
            ></v-text-field>
            <v-row>
             <v-text-field
              class="input"
              v-model="lat"
              :error-messages="latErrors"
              label="Latitude"
              required
              @input="$v.lat.$touch()"
              @blur="$v.lat.$touch()"
              filled
              rounded
              dense
            ></v-text-field>

             <v-text-field
              class="input"
              v-model="long"
              :error-messages="longErrors"
              label="Longitude"
              required
              @input="$v.long.$touch()"
              @blur="$v.long.$touch()"
              filled
              rounded
              dense
            ></v-text-field>
            </v-row>
            <v-text-field
              class="input"
              v-model="price"
              :error-messages="priceErrors"
              required
              label="Preço"
              prepend-icon="mdi-currency-eur"
              @input="$v.price.$touch()"
              @blur="$v.price.$touch()"
              filled
              rounded
              dense
            ></v-text-field>
            <v-row>
              <v-text-field
                v-model="timei"
                class="input"
                label="Horário de Inicio"
                :error-messages="timeiErrors"
                required
                prepend-icon="mdi-calendar-clock"
                @input="$v.timei.$touch()"
                @blur="$v.timei.$touch()"
                filled
                rounded
                dense
              ></v-text-field>
              <v-text-field
                v-model="timef"
                class="input"
                label="Horário de Fim"
                :error-messages="timefErrors"
                required
                prepend-icon="mdi-calendar-clock"
                @input="$v.timef.$touch()"
                @blur="$v.timef.$touch()"
                filled
                rounded
                dense
              ></v-text-field>
            </v-row>

            <v-file-input label="Imagens" filled prepend-icon="mdi-camera" rounded dense></v-file-input>
            <v-textarea
              v-model="obs"
              class="input-7-1"
              label="Observações"
              required
              filled
              rounded
              dense
            ></v-textarea>
            <div class="signup">
              <v-btn @click="handleSave" :disabled='!isComplete' depressed rounded x-large dark>
                <b>Guardar Garagem</b>
                <v-icon class="icon">far fa-save</v-icon>
              </v-btn>
            </div>
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
import { required } from "vuelidate/lib/validators";

export default {
  name: "AddGarage",
  mixins: [validationMixin],
  validations: {
    name:{required},
    address: { required },
    city: { required },
    lat: { required },
    long: { required },
    price: { required },
    timei: { required },
    timef: { required },
    description: {}
  },

  data() {
    return {
      alert:false,
      name:"",
      address: "",
      city:"",
      lat: "",
      long:"",
      price: "",
      timei: "",
      timef: "",
      owner: "",
      description: ""
    };
  },

  computed: {
    isComplete () {
    return this.name && this.address && this.city && this.lat && this.long;
  },
    timefErrors() {
      const errors = [];
      if (!this.$v.timef.$dirty) return errors;
      !this.$v.timef.required && errors.push("Campo obrigatório");
      return errors;
    },
    timeiErrors() {
      const errors = [];
      if (!this.$v.timei.$dirty) return errors;
      !this.$v.timei.required && errors.push("Campo obrigatório");
      return errors;
    },

    addressErrors() {
      const errors = [];
      if (!this.$v.address.$dirty) return errors;
      !this.$v.address.required && errors.push("Campo obrigatório");
      return errors;
    },
    priceErrors() {
      const errors = [];
      if (!this.$v.price.$dirty) return errors;
      !this.$v.price.required && errors.push("Campo obrigatório");
      return errors;
    },
    latErrors() {
      const errors = [];
      if (!this.$v.lat.$dirty) return errors;
      !this.$v.lat.required && errors.push("Campo obrigatório");
      return errors;
    },
    nameErrors() {
      const errors = [];
      if (!this.$v.name.$dirty) return errors;
      !this.$v.name.required && errors.push("Campo obrigatório");
      return errors;
    },
    cityErrors() {
      const errors = [];
      if (!this.$v.city.$dirty) return errors;
      !this.$v.city.required && errors.push("Campo obrigatório");
      return errors;

    },
    longErrors() {
      const errors = [];
      if (!this.$v.long.$dirty) return errors;
      !this.$v.long.required && errors.push("Campo obrigatório");
      return errors;
    }
  },

  methods: {
    /* eslint-disable no-console */
    handleSave(){
      this.save();
      this.isSignUP();
    },

    save() {
      this.$http
        .post(
          "http://spotnow.westeurope.cloudapp.azure.com:8000/api/garage-add/",
          {
            "name": this.name,
            "address": this.address,
            "city": this.city,
            "latitude": this.lat,
            "longitude": this.long,
            "preco":this.price,
            "owner": this.owner=3,
            
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
  height: 1100px;
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
  height: 100%;
  margin-left: 100px;
  margin-right: 100px;
  margin-top: 25px;
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

.input2 {
  margin: auto;
  max-width: 100%;
  max-height: 25%;
}

.signup {
  margin: auto;
  padding-top: 15px;
  padding-bottom: 15px;
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