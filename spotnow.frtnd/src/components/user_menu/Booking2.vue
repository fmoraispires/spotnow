<template>
<div>
  <div class="container">
    <div class="intro-text">
      <div class="intro-heading text-uppercase">Reserve o seu Lugar de Estacionamento</div>
    </div>
     <v-card flat tile class="card">
          <form class="form">
            <div class="card-title">
              <b>Insira os dados da smartlock da sua garagem</b>
            </div>
             <v-text-field
              class="input"
              v-model="time"
              :error-messages="timeErrors"
              label="Quanto tempo pretende reservar?"
              required
              @input="$v.time.$touch()"
              @blur="$v.time.$touch()"
              filled
              rounded
              dense
            ></v-text-field>
            <v-text-field
              class="input2"
              v-model="payment"
              :error-messages="paymentErrors"
              label="Tipo de Pagamento"
              required
              @input="$v.payment.$touch()"
              @blur="$v.payment.$touch()"
              filled
              rounded
              dense
            ></v-text-field>
            <div class="signup">
              <v-btn @click="handleBook" :disabled='!isComplete' depressed rounded x-large dark>
                <b>Reservar Garagem</b>
                <v-icon class="icon">far fa-save</v-icon>
              </v-btn>
            </div>
             <v-alert
          :value="alert"
          type="success"
          dismissible
          transition="scale-transition"
        >Reserva efectuada</v-alert>
          </form>
      <div class="fill-height" >
        <div class="intro-lead-in"><b>Utilize os botões para interagir com a porta da garagem</b></div>
        <v-btn :disabled='!isBookingDone'  dark  rounded x-large @click="OpenGarage" class="btn1"><v-icon size="50px">mdi-garage-open</v-icon><b>Abrir</b></v-btn>
        
        <v-btn :disabled='!isBookingDone'  dark x-large rounded  @click="CloseGarage" class="btn1"><v-icon size="50px">mdi-garage</v-icon><b>Fechar</b></v-btn>
      </div>
    </v-card>
  </div>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required } from "vuelidate/lib/validators";

export default {
  name: "Booking",
   mixins: [validationMixin],
  validations: {
    time:{required},
    payment: { required },
  },
  data() {
    return {
      garage: null,
      alert:false,
      state:false,
      time:"",
      payment: "",
    }
  },

  computed:{ 
    isBookingDone(){
      return this.alert;
    },

     isComplete () {
    return this.time && this.payment;
  },
  timeErrors() {
      const errors = [];
      if (!this.$v.time.$dirty) return errors;
      !this.$v.time.required && errors.push("Campo obrigatório");
      return errors;
    },
  paymentErrors() {
      const errors = [];
      if (!this.$v.payment.$dirty) return errors;
      !this.$v.payment.required && errors.push("Campo obrigatório");
      return errors;
    },
  },

  methods: {
    /* eslint-disable no-console */
     handleBook(){
      this.book();
      this.isSignUP();
    },

    book() {
// "state": "string",
//   "receipt": 0,
//   "garage": 0

      this.$http
        .post(
          "http://spotnow.westeurope.cloudapp.azure.com:8000/api/booking-add/",
          {
            "state": this.state,
            "receipt": this.owner=5,
            "garage": this.garage=1,

            
          }
        )
        .then(response => console.log(response));
      
    },
    isSignUP(){
      this.alert = true;
    return this.alert;
  },

    OpenGarage(){
      this.garage = true;
      //rasp 1 = 3badb453325ec958c339e55e;
      //rasp 2 = 560c6019872b960209c6cc02;
      //rasp 3 = b61dc354fa18a582717b6f1b;
      this.$http
          .post("http://spotnow.westeurope.cloudapp.azure.com:8000/api/smartlock-command/", 
            { "token":"560c6019872b960209c6cc02",
              "msg": "OPEN"})
          .then(response => console.log(response));


    },
    CloseGarage(){
      this.garage = false;
      this.$http
          .post("http://spotnow.westeurope.cloudapp.azure.com:8000/api/smartlock-command/", 
          { "token":"560c6019872b960209c6cc02",
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
  padding-bottom:25px;
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
    height: 600px;
    width:600px;
    margin: auto;
    padding-bottom: 50px;
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

.card-title2 {
  padding-top: 20px;
  padding-bottom: 30px;
  font-size: 22px;
  font-style: italic;
  line-height: 22px;
  margin: auto;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
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
}

.icon {
  margin-left: 5px;
}


.fill-height{
  padding-top:80px;
  padding-bottom:25px;

}



.btn1{
    align-items: center;
    margin-left: 40px;
    padding-left: 40px;
    padding-top: 20px;

}
</style>