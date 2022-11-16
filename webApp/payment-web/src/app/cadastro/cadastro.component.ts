import { Component, OnInit } from '@angular/core';
import { CadastroService, IAllPayments, INewPayment } from './cadastro.service';
import { FormGroup, Validators } from '@angular/forms';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})
export class CadastroComponent implements OnInit {
  form!: FormGroup;

  userSourcer: IAllPayments[] = [];
  newUser: INewPayment = {} as INewPayment
  uploadedFiles: any[] = [];

  constructor(
    private cadastroService: CadastroService,
    private formBuilder: FormBuilder,
  ) { }

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

  InputUsuario() {
    this.newUser.payer_name = this.form.value.payer_name
    this.newUser.card_number = this.form.value.card_number
    this.newUser.zip_code = this.form.value.zip_code
    this.newUser.payment_value = this.form.value.payment_value
    this.cadastroService
      .cadastrarUsuario(this.newUser)
      .subscribe(() => {
        this.listAllUsers();
      }
      );

  }


}
