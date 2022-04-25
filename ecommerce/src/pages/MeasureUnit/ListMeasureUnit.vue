<template>
  <div class="q-pa-xl">
<!--    separator="cell"-->
<!--    class="col"-->
    <q-table

      title="Unidad de Medida"
      :rows="rows"
      :columns="columns"
      row-key="id"
      :selected-rows-label="getSelectedString"
      selection="multiple"
      v-model:selected="selected"
      >
      <template v-slot:body-cell-action="props">
        <q-td :props="props">

          <q-btn
            round
            outline
            color="blue"
            glossy
            icon="edit"
            @click="editMeasureUnit(props.row.id)"
          />
          <q-btn
            round
            outline
            color="red"
            glossy
            icon="delete"
            class="q-ml-sm"
            @click="deleteMeasureUnit(props.row.id)"
          />

        </q-td>
      </template>

    </q-table>
  </div>
</template>

<script>
import { ref } from 'vue'
import { defineComponent } from 'vue'

import axios from "axios";

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

export default defineComponent({
  name: 'ListMeasureUnit',

  data(){
    const selected = ref([])
    return{
      measureUnitId: this.$route.params.measureUnitId,
      columns:[
        {
        name: 'id',
        required: true,
        label: 'ID',
        align: 'left',
        field: 'id',
        sortable: true
    },
        {
        name: 'description',
        required: false,
        label: 'Description',
        align: 'center',
        field: 'description',
        sortable: true
    },
        {
        name: 'action',
        label: 'Action',
        align: 'center',
        sortable: true
    }
      ],
      rows:[],
      selected:[],
      // getSelectedString () {
      //   return selected.value.length === 0 ? '' : `${selected.value.length} record${selected.value.length > 1 ? 's' : ''} selected of ${rows.length}`
      // }
    }
  },
  mounted(){
    this.getRows();
  },
  methods: {
    getRows(){
      this.$axios.get('http://localhost:8000/products/measure_units/')
      .then(res=>{
        this.rows = res.data;
      })
      .catch(err=>{
        console.log(err)
      })
    },
    // editMeasureUnit(idMeasure){
    //   console.log(idMeasure)
    // },
    editMeasureUnit(measureUnitId){
      const path = `http://localhost:8000/products/measure_units/${measureUnitId}/`      
      
      // this.$axios.put(`http://localhost:8000/products/measure_units/${measureUnitId}/`)
      this.$axios.put(path, this.columns).then((response) => {
        this.columns.description = response.data.description;

        this.columns.description = '';
      })
      .then(res=>{
        this.rows = res.data;
        console.log(this.rows)
      })
      .catch(err=>{
        console.log(err)
      })
    },
    deleteMeasureUnit(idMeasure){
      console.log(idMeasure)
    }
  }
})
</script>
