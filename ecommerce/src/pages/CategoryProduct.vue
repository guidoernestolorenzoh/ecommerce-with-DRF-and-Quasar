<template>
  <div class="q-pa-xl">
    <q-table

      title="Categoria de Productos"
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
            @click="editCategoryProduct(props.row.id)"
          />
          <q-btn
            round
            outline
            color="red"
            glossy
            icon="delete"
            class="q-ml-sm"
            @click="deleteCategoryProduct(props.row.id)"
          />

        </q-td>
      </template>

    </q-table>

<!--    <q-dialog v-model="showDialog">-->
<!--      <div />-->
<!--    </q-dialog>-->

    <div class="q-pa-xl" align="right">
      <q-btn
        class="floating-button-add"
        round
        color="blue"
        icon="add"
        @click="add_categ_prod"
      />

    </div>

  </div>
</template>

<script>
import { ref } from 'vue'
import { defineComponent } from 'vue'
import {useQuasar} from "quasar";

export default defineComponent({
  name: 'IndexPage',

  data(){
    const selected = ref([])

    const $q = useQuasar()
    const description = ref()


    function add_categ_prod(){
      $q.dialog({
        title: 'Add Category Product',
        message: 'Description',
        prompt: {
          model:'',
          type:'text',
        },
        cancel:true,
        persistent:true
      }).onOk(data => {

        description.value = data
        console.log(description.value);
      }).onCancel(() => {
        console.log('Cancel')
      })
      //   .onDismiss(() => {
      //   console.log('Dismiss')
      // })
    }

    return{
      add_categ_prod,
      description,
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
      this.$axios.get('http://localhost:8000/products/category_products/')
      .then(res=>{
        this.rows = res.data;
      })
      .catch(err=>{
        console.log(err)
      })
    },
    editCategoryProduct(idCategoryProd){
      console.log(idCategoryProd)
    },
    deleteCategoryProduct(idCategoryProd){
      console.log(idCategoryProd)
    }
  }
})
</script>

