import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { SafeUrl } from '@angular/platform-browser';

export interface IAllPayments {
  authorization_timestamp: string;
  card_number: string;
  payer_name: string;
  payment_id: number;
  payment_value: number;
  status: string;
  status_code: number;
  zip_code: string;
}


export interface INewPayment {
  payer_name: string;
  card_number: number;
  payment_value: number;
  zip_code: number
}



@Injectable({
  providedIn: 'root',
})

export class CadastroService {
  pathUrlBase = 'http://localhost:8000'
  constructor(private http: HttpClient) { }



  listarTodosUsuarios(): Observable<IAllPayments[]> {
    return this.http.get<IAllPayments[]>(
      `${this.pathUrlBase}/payments`
    );
  }




  cadastrarUsuario(
    newPayment: INewPayment
  ): Observable<IAllPayments> {
    return this.http.post<IAllPayments>(
      `${this.pathUrlBase}/payment`,
      { ...newPayment }
    );
  }

  updatePagamento(
    payment_id: number,
    new_status_code: number
  ): Observable<IAllPayments> {
    console.log(payment_id)
    return this.http.patch<IAllPayments>(
      `${this.pathUrlBase}/payment`,
      { payment_id, new_status_code }
    );
  }



}



