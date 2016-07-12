int foo(int a[],int len)
{
  int result=0;
  for(int i=0;i<len;i++)
  {
    a[i]=10*a[i];
    result+=a[i];
  }
  return result;
}

//int * add1(int a[])
//{
//  int b[3];
//  for (int i = 0; i < 3; i++)
//  {
//    b[i] = a[i] + 1;
//  }
//
//  return b;
//}
