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

  // listaUsuarioPorId(
  //   id: number
  // ): Observable<IAllUsers> {
  //   return this.http.post<IAllUsers>(
  //     `${this.pathUrlBase}/users`,
  //     { id }
  //   );
  // }



  cadastrarUsuario(
    newPayment: INewPayment
  ): Observable<IAllPayments> {
    console.log(newPayment)
    return this.http.post<IAllPayments>(
      `${this.pathUrlBase}/payment`,
      { ...newPayment }
    );
  }

}



