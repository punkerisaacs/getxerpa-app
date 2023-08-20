import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { WebApiService } from './web-api.service';

var apiUrl = "http://127.0.0.1:8000";

var httpLink = {
  getCategories: apiUrl + "/api/category/",
}
@Injectable({
  providedIn: 'root'
})
export class HttpProviderService {
  constructor(private webApiService: WebApiService) { }

  public getCategories(): Observable<any> {
    return this.webApiService.get(httpLink.getCategories);
  }
  public getCategory(categoryId: number): Observable<any> {
    return this.webApiService.get(`${httpLink.getCategories}${categoryId}/`);
  }
  public getCategoryTransactions(categoryId: number): Observable<any> {
    return this.webApiService.get(`${httpLink.getCategories}${categoryId}/transaction`);
  }
}                          