import { Component, OnInit } from '@angular/core';
import { CadastroService, IAllPayments, INewPayment } from './cadastro.service';
import { FormGroup, Validators } from '@angular/forms';
import { FormBuilder } from '@angular/forms';
import { MessageService } from 'primeng/api';

interface Status {
  status_code: number,
  status: string
}
@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css'],
  providers: [MessageService]
})

export class CadastroComponent implements OnInit {
  form!: FormGroup;

  userSourcer: IAllPayments[] = [];
  newUser: INewPayment = {} as INewPayment
  uploadedFiles: any[] = [];

  status: Status[] = [];
  selectedstatus!: string;


  constructor(
    private cadastroService: CadastroService,
    private formBuilder: FormBuilder,
    private messageService: MessageService
  ) {
    this.status = [
      {
        status_code: 1, status: 'Created'
      },
      {
        status_code: 2, status: 'processing'
      },
      {
        status_code: 3, status: 'finished'
      },
    ]
  }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      payer_name: [null, Validators.required],
      card_number: [null, Validators.required],
      zip_code: [null, Validators.required],
      payment_value: [null, Validators.required]
    });
    this.listAllUsers();
  }


  listAllUsers() {
    this.cadastroService
      .listarTodosUsuarios()
      .subscribe((resp) => {
        this.userSourcer = resp;
      });

  }

  inputUsuario() {
    this.newUser.payer_name = this.form.value.payer_name
    this.newUser.card_number = this.form.value.card_number
    this.newUser.zip_code = this.form.value.zip_code
    this.newUser.payment_value = this.form.value.payment_value
    this.cadastroService
      .cadastrarUsuario(this.newUser)
      .subscribe(() => {
        this.messageService.add({ severity: 'success', summary: 'Feito!', detail: 'Pagamento Cadastrado!' });
        this.form.reset();
        this.listAllUsers();
      }
      );

  }

  alteraPagamento(pagamento: IAllPayments, new_status_code: number ) {
    console.log(pagamento)
    this.cadastroService
      .updatePagamento(pagamento.payment_id, new_status_code)
      .subscribe(() => {
        this.messageService.add({ severity: 'success', summary: 'Feito!', detail: 'Pagamento Alterado' });
        this.listAllUsers();
      }
      )
  }


}
