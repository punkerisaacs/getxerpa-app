import { Component, Input, OnInit, Type } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { HttpProviderService } from '../Service/http-provider.service';
import * as _ from 'lodash';
import * as moment from 'moment';

@Component({
  selector: 'app-category-detail',
  templateUrl: './category-detail.component.html',
  styleUrls: ['./category-detail.component.scss']
})
export class CategoryDetailComponent implements OnInit {
  closeResult = '';
  categoryId: any;
  category: any = {};
  transactions: any = [];
  constructor( private route: ActivatedRoute, private router: Router,
    private toastr: ToastrService, private httpProvider : HttpProviderService) { }

  ngOnInit(): void {
    this.categoryId = this.route.snapshot.params['categoryId'];
    this.getCategory();
    this.getTransactions();
  }
  async getCategory() {
    this.httpProvider.getCategory(this.categoryId).subscribe((data : any) => {
      if (data != null && data.body != null) {
        var resultData = data.body;
        if (resultData) {
          this.category = resultData;
        }
      }
    },
    (error : any)=> {
        if (error) {
          if (error.status == 404) {
            if(error.error && error.error.message){
              this.category = {};
            }
          }
        }
      });
  }
  async getTransactions() {
    this.httpProvider.getCategoryTransactions(this.categoryId).subscribe((data : any) => {
      if (data != null && data.body != null) {
        var resultData = data.body;
        if (resultData) {
          let groups = _.groupBy(resultData, function (transaction: any) {
            console.log(transaction)
            return moment(transaction.date).startOf('day').format();
          });

          var result = _.map(groups, function(group: any, day:any){
            return {
                day: moment(day).isSame(moment(), 'day') ? 'today' : moment(day).format('DD MMMM') ,
                transactions: group,
                date: day
            }

        });

        const sort = _.sortBy(result, function(dateObj) {
          return dateObj.date;
        }).reverse()

          this.transactions = sort;
        }
      }
    },
    (error : any)=> {
        if (error) {
          if (error.status == 404) {
            if(error.error && error.error.message){
              this.transactions = [];
            }
          }
        }
      });
  }
}
