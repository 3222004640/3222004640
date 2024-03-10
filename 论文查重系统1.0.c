#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#define  max_number  1024
//计算每一块相似字数
size_t char_compare(char*org, size_t sum1, char*org_add, size_t sum2, size_t count)
{
	size_t i = 0, j = 0;
	while (i < sum1) {
		j = 0; // 重置j，以便每次从org_add的开始处进行比较  
		while (j < sum2) {
			if (org[i] == org_add[j]) {
				// 找到匹配的字符，增加count并跳出内部循环  
				if (org[i] != ' '&&org[i] != ','&&org[i] != ','&&org[i] != '!'&&org[i] != ':');
				count++;
				break;
			}
			j++; // 继续在org_add中查找  
		}
		i++; // 无论是否找到匹配项，都继续检查org中的下一个字符  
	}
	return count; // 
}


int main(int argc,char*argv[])
{
	
	if (argc < 4) {
		printf("Usage: %s file1 file2\n", argv[0]);
		return 1;
	}
	FILE *fp = fopen(argv[1], "rb");
	if (fp == NULL)
	{
		printf("failed to open file1\n");
		return 0;
	}
	FILE *fp1 = fopen(argv[2], "rb");
	if (fp1 == NULL)
	{
		printf("failed to open file2\n");
		return 0;
	}
	//开辟动态空间给缓存区
	char *buffer1 = malloc(max_number * sizeof(char));
	char *buffer2 = malloc(max_number * sizeof(char));
	//判断空间是否成功
	if (buffer1 == NULL)
	{
		printf("ERROR\n");
		fclose(fp);
		fclose(fp1);
		return 0;
	}
	if (buffer2 == NULL)
	{
		printf("ERROR\n");
		fclose(fp);
		fclose(fp1);
		free(buffer1);
		return 0;
	}
	size_t size1, size2;//每一块字数
	size_t Count = 0;//重复字数
	size_t total, total1, total2;//两文件字数最多的那个、文件1字数、文件2字数
	total = 0; total1 = 0; total2 = 0;
	do {
		size1 = fread(buffer1, sizeof(char), max_number, fp);//将文件的内容读取到缓存区中
		size2 = fread(buffer2, sizeof(char), max_number, fp1);
		// 遍历缓冲区并比较字符  
		Count = char_compare(buffer1, size1, buffer2, size2, Count);
		total1 += size1;
		total2 += size2;
	} while (size1 != 0 && size2 != 0);
	free(buffer1);
	free(buffer2);
	total = total1 > total2 ? total1 : total2;
	float similarity;//相似度
	similarity = (float)Count / total;
	char buffer[50]; // 足存储小数转换为字符串后的结果    
	snprintf(buffer, sizeof(buffer), "%0.2f", similarity);
	FILE *fp2 = fopen(argv[3], "w");
	if (fp2 == NULL)
	{
		printf("failed to open file3\n");
		return 0;
	}
	fputs(buffer, fp2);
	// 释放空间
	fclose(fp);
	fclose(fp1);
	fclose(fp2);
	return 0;
}