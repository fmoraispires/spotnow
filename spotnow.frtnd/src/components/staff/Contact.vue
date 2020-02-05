<template>
  <div id="contacts">
    <ul>
      Owners:
      <li v-for="owner in owners" v-bind:key="owner" v-text="owner.user_obj.username"></li>
    </ul>
    <ul>
      Clients:
      <li v-for="client in clients" v-bind:key="client" v-text="client.user_obj.username"></li>
    </ul>
    <ul>
      Garage:
      <li v-for="garage in garages" v-bind:key="garage" v-text="garage.name"></li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      owners: null,
      clients: null,
      garages: null,
    };
  },
  /* eslint-disable no-console */
  mounted: function() {
    // this.$http
    //   .post(
    //     "http://spotnow.westeurope.cloudapp.azure.com:8000/api/owner-add/",
    //     {
    //       // "user": {
    //       //   "username": "owner3",
    //       //   "password": "owner3spotnow",
    //       //   "email": "owner3@gmail.com"
    //       // },
    //       // "nif": "1234",
    //       // "telephone": "1234"
    //     }
    //   )
    //   .then(response => console.log(response));

    this.$http
      .get("http://spotnow.westeurope.cloudapp.azure.com:8000/api/owners/")
      .then(response => (this.owners = response.data))
      .finally(() => console.log("ola"));

    

    
    this.$http
      .get("http://spotnow.westeurope.cloudapp.azure.com:8000/api/clients/")
      .then(response => (this.clients = response.data))
      .finally(() => console.log("ola"));

       this.$http
      .get("http://spotnow.westeurope.cloudapp.azure.com:8000/api/garages/")
      .then(response => (this.garages = response.data))
      .finally(() => console.log("ola"));
  }
  /* eslint-enable no-console */
};
</script>

<style scoped>
.section-heading {
  font-size: 40px;
  margin-top: 0;
  margin-bottom: 15px;
}

h3.section-subheading {
  font-size: 16px;
  font-weight: 400;
  font-style: italic;
  margin-bottom: 75px;
  text-transform: none;
  font-family: "Montserrat", "Helvetica Neue", Helvetica, sans-serif;
}

.topic-heading {
  margin: 15px 0;
}
</style>